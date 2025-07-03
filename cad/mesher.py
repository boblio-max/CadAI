import numpy as np
import pyvista as pv
from utils.logger import logger

def create_mesh_from_points(points: list[tuple[float, float, float]]) -> pv.PolyData:
    """
    Creates a 3D mesh from a list of points using Delaunay triangulation.

    Args:
        points: A list of (x, y, z) tuples.

    Returns:
        A pyvista.PolyData object representing the mesh.
    """
    if not points:
        logger.warning("Point list is empty. Cannot create a mesh.")
        return pv.PolyData()

    try:
        point_cloud = pv.PolyData(np.array(points))
        mesh = point_cloud.delaunay_3d()
        logger.info("Successfully created a 3D mesh from the point cloud.")
        return mesh
    except Exception as e:
        logger.error(f"Failed to create mesh from points: {e}")
        return pv.PolyData()

def export_mesh_to_stl(mesh: pv.PolyData, filename: str):
    """
    Exports a mesh to an STL file.

    Args:
        mesh: The pyvista.PolyData mesh to export.
        filename: The name of the output STL file.
    """
    if not mesh.n_points:
        logger.error("Cannot export an empty mesh.")
        return

    try:
        mesh.save(filename)
        logger.info(f"Successfully exported the mesh to {filename}")
    except Exception as e:
        logger.error(f"Failed to export mesh to STL: {e}")
