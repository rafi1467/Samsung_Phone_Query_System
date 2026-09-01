import sys
import os

# Project root add
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from rag.search_phone import get_phone


def specification_agent(phone_name):
    return get_phone(phone_name)


def review_agent(phone):

    review = f"""
Review of {phone['name']}

Display:
{phone['display_size']}

Performance:
Powered by {phone['chipset']}.

Battery:
{phone['battery']}

Charging:
{phone['charging']}

Overall Verdict:
A premium Samsung smartphone with strong performance,
excellent battery life and flagship-level features.
"""

    return review


phone = specification_agent("S24")

print(review_agent(phone))