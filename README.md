# AI CAD Generator

This application generates 3D models from a natural language description using a generative AI model. It creates a point cloud based on the user's prompt, converts it into a 3D mesh, and provides an interactive visualization. The generated model can also be exported to an STL file.

## Features

-   **AI-Powered 3D Model Generation:** Describe an object in plain English and have the AI generate a 3D representation.
-   **Point Cloud to Mesh Conversion:** Automatically converts the generated point cloud into a solid 3D mesh.
-   **Interactive 3D Viewer:** Rotate, pan, and zoom the 3D model to inspect it from all angles.
-   **STL Export:** Save your creations as STL files for use in other 3D applications or for 3D printing.
-   **User-Friendly Command-Line Interface:** Easy-to-use commands for generating and exporting models.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-cad-generator.git](https://github.com/your-username/ai-cad-generator.git)
    cd ai-cad-generator
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To generate and visualize a 3D model, run the following command:

```bash
python main.py "a simple cube"
