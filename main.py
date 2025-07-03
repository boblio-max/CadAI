import argparse
from cad.generator import generate_points_from_prompt
from cad.mesher import create_mesh_from_points, export_mesh_to_stl
from cad.visualizer import visualize_mesh
from utils.logger import logger

def main():
    """
    The main function for the AI CAD Generator.
    """
    parser = argparse.ArgumentParser(description="AI CAD Generator")
    parser.add_argument("prompt", type=str, help="A description of the 3D object to generate.")
    parser.add_argument("--export", type=str, help="Export the generated model to an STL file.")
    args = parser.parse_args()

    logger.info(f"Generating model for prompt: '{args.prompt}'")

    points = generate_points_from_prompt(args.prompt)
    if not points:
        logger.error("Could not generate points. Exiting.")
        return

    mesh = create_mesh_from_points(points)
    if not mesh.n_points:
        logger.error("Could not create a mesh. Exiting.")
        return

    if args.export:
        export_mesh_to_stl(mesh, args.export)

    visualize_mesh(mesh)

if __name__ == "__main__":
    main()
