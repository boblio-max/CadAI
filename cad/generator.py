import json
from g4f.client import Client
from utils.logger import logger

def generate_points_from_prompt(prompt: str) -> list[tuple[float, float, float]]:
    """
    Generates a list of 3D points from a natural language prompt using a generative AI model.

    Args:
        prompt: The user's description of the object.

    Returns:
        A list of (x, y, z) tuples representing the point cloud.
    """
    client = Client()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Based on the prompt '{prompt}', generate a list of 3D points (x, y, z) that form the described object. The points should be in a JSON format as a list of lists, like [[x1, y1, z1], [x2, y2, z2], ...]. Generate a sufficient number of points to represent the object's surface. Only provide the JSON data.",
                }
            ],
            web_search=False,
        )
        points_json = response.choices[0].message.content
        points = json.loads(points_json)
        logger.info(f"Successfully generated {len(points)} points.")
        return [tuple(p) for p in points]
    except Exception as e:
        logger.error(f"Failed to generate or parse points from the AI model: {e}")
        return []
