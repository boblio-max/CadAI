import pyvista as pv
from utils.logger import logger

def visualize_mesh(mesh: pv.PolyData):
    """
    Displays a 3D mesh in an interactive window.

    Args:
        mesh: The pyvista.PolyData mesh to visualize.
    """
    if not mesh.n_points:
        logger.error("Cannot visualize an empty mesh.")
        return

    try:
        plotter = pv.Plotter(window_size=[800, 600])
        plotter.add_mesh(mesh, show_edges=True, color="lightblue")
        plotter.add_axes()
        plotter.camera_position = "iso"
        logger.info("Displaying the 3D model. Close the window to exit.")
        plotter.show()
    except Exception as e:
        logger.error(f"Failed to visualize the mesh: {e}")
