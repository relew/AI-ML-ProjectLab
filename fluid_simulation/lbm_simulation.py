import matplotlib.pyplot as plt
import numpy as np

plot_every = 100  # Defines how often the simulation will plot the velocity field

def distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two points (x1, y1) and (x2, y2).
    This is used to determine which cells belong to the cylinder boundary.
    """
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    """ 
    Lattice Boltzmann Simulation using D2Q9 (2D, 9 velocities model). 
    The goal is to simulate fluid flow around a cylindrical obstacle using the Lattice Boltzmann Method (LBM).
    """

    # Simulation parameters
    Nx = 400    # Number of grid points in the x-direction (horizontal resolution)
    Ny = 100    # Number of grid points in the y-direction (vertical resolution)
    tau = 0.65   # Relaxation time for collision (controls the viscosity of the fluid)
    Nt = 5000   # Number of timesteps for the simulation
    plotRealTime = True  # Whether to plot the velocity field in real-time as the simulation runs
    
    # Lattice speeds and corresponding weights for the D2Q9 model (9 directions)
    NL = 9  # Number of lattice directions (D2Q9 has 9 discrete velocities)
    idxs = np.arange(NL)  # Array of indices for the directions
    cxs = np.array([0, 0, 1, 1, 1, 0, -1, -1, -1])  # x-components of the discrete velocity directions
    cys = np.array([0, 1, 1, 0, -1, -1, -1, 0, 1])  # y-components of the discrete velocity directions
    weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])  # Weights for each velocity direction (must sum to 1)
    
    # Initial Conditions: 
    # F is the distribution function that contains particle populations at each grid point for each velocity direction
    F = np.ones((Ny, Nx, NL)) + 0.01 * np.random.randn(Ny, Nx, NL)  # Slightly perturb the initial density to introduce turbulence
    F[:, :, 3] = 2.3  # Bias the initial distribution to introduce some flow in the positive x-direction (inlet flow)
    
    # Cylinder Obstacle: create a mask for the cylinder in the grid
    cylinder = np.full((Ny, Nx), False)  # Boolean mask representing the cylinder (False means no obstacle)
    cylinder_diameter = 13  # Diameter of the cylinder
    # Iterate over the grid and mark the points that belong to the cylinder
    for y in range(0, Ny):
        for x in range(0, Nx):
            if distance(Nx//4, Ny//2, x, y) < cylinder_diameter:  # If within the cylinder radius, mark it as part of the obstacle
                cylinder[y, x] = True

    # Main loop: This loop runs the simulation for Nt timesteps
    for it in range(Nt):
        # print(it)  # Print the current timestep for monitoring progress

        # Boundary Conditions: Set reflective boundary conditions on the left (inlet) and right (outlet) boundaries
        F[:, -1, [6, 7, 8]] = F[:, -2, [6, 7, 8]]  # Reflect the distributions at the outlet (right boundary)
        F[:, 0, [2, 3, 4]] = F[:, 1, [2, 3, 4]]   # Reflect the distributions at the inlet (left boundary)

        # Streaming Step: Move particles to their neighboring cells based on their velocity directions (lattice shift)
        for i, cx, cy in zip(range(NL), cxs, cys):
            F[:, :, i] = np.roll(F[:, :, i], cx, axis=1)  # Shift the distribution along the x-direction
            F[:, :, i] = np.roll(F[:, :, i], cy, axis=0)  # Shift the distribution along the y-direction

        # Apply boundary conditions to the cylinder obstacle
        # Reverse the direction of incoming particles at the obstacle boundary (bounce-back rule)
        bndryF = F[cylinder, :].copy()  # Copy the distributions at the cylinder boundary to apply boundary conditions
        bndryF = bndryF[:, [0, 5, 6, 7, 8, 1, 2, 3, 4]]  # Reverse the directions of the distribution at the boundary (bounce-back)
        
        # Calculate macroscopic fluid variables (density and velocity)
        rho = np.sum(F, axis=2)  # Fluid density (summed over all velocity directions)
        ux = np.sum(F * cxs, axis=2) / rho  # x-component of fluid velocity (momentum in x-direction divided by density)
        uy = np.sum(F * cys, axis=2) / rho  # y-component of fluid velocity (momentum in y-direction divided by density)

        # Set velocity to zero inside the cylinder (no fluid flow inside the obstacle)
        F[cylinder, :] = bndryF  # Apply bounce-back boundary conditions to the cylinder
        ux[cylinder] = 0  # Set x-velocity to zero inside the cylinder
        uy[cylinder] = 0  # Set y-velocity to zero inside the cylinder

        # Collision Step: Apply the Lattice Boltzmann collision operator (relaxation toward equilibrium)
        Feq = np.zeros(F.shape)  # Initialize the equilibrium distribution function
        # Compute the equilibrium distribution based on the current macroscopic variables (rho, ux, uy)
        for i, cx, cy, w in zip(range(NL), cxs, cys, weights):
            Feq[:, :, i] = rho * w * (
                1 + 3 * (cx * ux + cy * uy) +  # First-order term (linear velocity)
                9 * (cx * ux + cy * uy)**2 / 2 -  # Second-order term (velocity squared)
                3 * (ux**2 + uy**2) / 2  # Energy term (velocity magnitude squared)
            )

        # Relaxation step: update the distribution function toward the equilibrium (collide step)
        F += -(1/tau) * (F - Feq)  # Perform the collision step with relaxation time tau

        # Real-time visualization: Plot the velocity field every 'plot_every' timesteps
        if it % plot_every == 0:
            plt.imshow(np.sqrt(ux**2 + uy**2))  # Plot the magnitude of the velocity field (sqrt(ux^2 + uy^2))
            plt.pause(0.01)  # Pause briefly to display the plot
            plt.cla()  # Clear the plot for the next timestep

if __name__ == "__main__":
    main()  # Run the main simulation function
