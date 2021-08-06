import json
import re
import openai
from chronological import read_prompt, cleaned_completion, main
from .constants import *
from .search_results_utils import *
from .FIND_POS import get_pos
from .Open_or_close import ClassifyAction
from .create_email_from_json import create_email_response
from .order import Order

async def call_gpt3(input_data):
    orders = await create_orders(input_data)
    response = create_email_response(orders)
    json_response = create_json_response(orders)
    print(json_response)
    return response

def create_json_response(orders):
    json_orders = [order.to_dict_item() for order in orders]
    d = {"orders": json_orders}
    print(d)
    return json.dumps(d)

async def create_orders(input_data):
    categories = await semantic_search_erl_erk(input_data)
    positions, _ = get_pos(input_data)
    action = ClassifyAction(input_data)
    pos = positions.keys()
    orders = [Order(po, categories, positions[po], action) for po in pos]
    return orders


async def classify_erl_erk(input_data):
    print("Here")
    prompt_extract_erk_info = prompt
    prompt_extract_erk_info += input_data
    completion_extract_erk_info = await cleaned_completion(prompt_extract_erk_info, max_tokens=200, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])

    m = re.search(r"\[([a-z,]+)\]", completion_extract_erk_info)
    return m.group(0).split(", ") if m else []

async def semantic_search_erl_erk(input_data):
    response = openai.Engine("davinci").search(
        search_model="davinci",
        query=input_data,
        documents=[
            "Endrechnungskennzeichen and Endlieferkennzeichen",
            "Endrechnungskennzeichen",
            "Endlieferkennzeichen"
            ]
    )

    search_results = create_search_results(response)
    if rel_diff_is_too_small(search_results):
        classify_result = await classify_erl_erk(input_data)
        if classify_result:
            return classify_result

    return search_results[0].type

async def logic(input_data):
    result = await classify_erl_erk(input_data)
    print(result)


# input_data = text_prompt
# main(logic(text_prompt))
