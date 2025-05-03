import matplotlib.pyplot as plt
import numpy as np

plot_every = 100

def distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    """ Lattice Boltzmann Simulation """

    # Simulation parameters
    Nx = 400    # resolution x-dir
    Ny = 100    # resolution y-dir
    tau = 0.7   # collision timescale
    Nt = 5000   # number of timesteps
    plotRealTime = True # switch on for plotting as the simulation goes along
    
    # Lattice speeds / weights
    NL = 9
    idxs = np.arange(NL)
    cxs = np.array([0, 0, 1, 1, 1, 0,-1,-1,-1])
    cys = np.array([0, 1, 1, 0,-1,-1,-1, 0, 1])
    weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36]) # sums to 1
    
    # Initial Conditions + Add random condition / turbulence 
    #np.random.seed(42)
    F = np.ones((Ny, Nx, NL)) + 0.01 * np.random.randn(Ny, Nx, NL)
    F[:, :, 3] = 2.3
    cylinder = np.full((Ny, Nx), False)
    cylinder_diameter = 13

    # Create the cylinder boundary
    for y in range(0,Ny):
        for x in range(0,Nx):
            if (distance(Nx//4, Ny//2, x, y) < cylinder_diameter):
                cylinder[y, x] = True

    # Main loop
    for it in range(Nt):
        print(it)

        F[:, -1, [ 6, 7, 8]] = F[:, -2, [ 6, 7, 8]]
        F[:,  0, [ 2, 3, 4]] = F[:,  1, [ 2, 3, 4]] 


        # Streaming step
        for i, cx, cy in zip(range(NL), cxs, cys):
            F[:, :, i] = np.roll(F[:, :, i], cx, axis=1)
            F[:, :, i] = np.roll(F[:, :, i], cy, axis=0)

        # Apply boundary conditions
        bndryF = F[cylinder, :]  # Copy to avoid overwriting
        bndryF = bndryF[:, [0, 5, 6, 7, 8, 1, 2, 3, 4]]

        # Fluid variables
        rho = np.sum(F, axis=2)  # Density
        ux = np.sum(F * cxs, axis=2) / rho  # x-momentum
        uy = np.sum(F * cys, axis=2) / rho  # y-momentum

        F[cylinder, :] = bndryF
        ux[cylinder] = 0
        uy[cylinder] = 0

        # Collision step
        Feq = np.zeros(F.shape)
        for i, cx, cy, w in zip(range(NL), cxs, cys, weights):
            Feq[:, :, i] = rho * w * (
                1 + 3 * (cx * ux + cy * uy) +
                9 * (cx * ux + cy * uy)**2 / 2 -
                3 * (ux**2 + uy**2) / 2
            )

        F = F + -(1/tau) * (F - Feq)

        # Plotting the velocity field
        if it % plot_every == 0:
            plt.imshow(np.sqrt(ux**2 + uy**2))
            plt.pause(0.01)
            plt.cla()

if __name__ == "__main__":
    main()
