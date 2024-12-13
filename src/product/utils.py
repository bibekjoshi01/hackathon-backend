import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def generate_product_description(product_name, category, additional_info=None):
    """
    Generate a product description using OpenAI API with the latest SDK version.
    """
    messages = [
        {
            "role": "system",
            "content": "You are a professional content generator specialized in creating SEO-friendly product descriptions in Nepali. Please generate the descriptions",
        },
        {
            "role": "user",
            "content": (
                f"Generate an SEO-friendly product description for the following:\n\n"
                f"Product Name: {product_name}\n"
                f"Category: {category}\n"
                f"{f'Additional Information: {additional_info}' if additional_info else ''}\n\n"
                "Description:"
            ),
        },
    ]

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=250,
            temperature=0.7,
        )
        description = response.choices[0].message.content.strip()
        return description
    except Exception as e:
        raise ValueError(f"Error generating description: {str(e)}")
