import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_groq import ChatGroq
import  streamlit as st

st.title("Review filter app")
# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM (ChatGroq)
llm = ChatGroq(
    model="llama3-8b-8192",  # or "llama3-8b-instruct" depending on your available model
    temperature=0,
    api_key=api_key
)

# Define the response schema
gift_schema = ResponseSchema(
    name="gift",
    description="Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown."
)
delivery_days_schema = ResponseSchema(
    name="delivery_days",
    description="How many days did it take for the product to arrive? If this information is not found, output -1."
)
price_value_schema = ResponseSchema(
    name="price_value",
    description="Extract any sentences about the value or price, and output them as a comma separated Python list."
)

# Combine schemas
response_schemas = [gift_schema, delivery_days_schema, price_value_schema]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

# Define the prompt template
review_template = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? Answer True if yes, False if not or unknown.
delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.
price_value: Extract any sentences about the value or price, and output them as a comma separated Python list.

text: {text}

{format_instructions}
"""

# Format the prompt with customer review
prompt = ChatPromptTemplate.from_template(review_template)
customer_review = st.text_input("enter your review")

if customer_review:

    messages = prompt.format_messages(
        text=customer_review,
        format_instructions=format_instructions
    )

    # Invoke the LLM
    response = llm.invoke(messages)

    st.write(response.content)
