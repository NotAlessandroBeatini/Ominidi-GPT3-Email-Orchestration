import os
import openai
from googletrans import Translator
#openai.api_key = ""

def ClassifyAction(mail):
    translator = Translator()
    query=translator.translate(mail, dest="en").text
    #myfile=openai.File.create(file=open("train.jsonl"), purpose="classifications")
    examples=[
        ["""Final invoice indicator. Please set the final invoice indicator in the following orders.

    9704530974
    9704679737 """, "Close"],
        ["""Close orders. Please set the final delivery and final invoice indicator for the following orders:
    9702677834
    9703867139
    9703667402""", "Close"],
        ["""AW: BZ9703507245. Please do not open again.


    Many Thanks.
    -----
    BZ9703507245
    Priority: high


    Please unlock BZ9703507245, then please send $ PERSON to Ms. $ PERSON so that the invoice can be posted.

    Many Thanks.""", "Open"],
    ["""Unlock orders. Can you please the orders.
    9703560077
    and
    9704113070
    unlock so that the invoices can be posted on it? ""","Open"],
    ["""1100 / invoicing.

    please remove the final invoice number.

    9705413421 696193
    9705413379 696280
    9705425846 696077

    thanks
    ""","Open"],
    ["""Final delivery hook and final invoice hook. would you please remove the final delivery check mark and final invoice check mark in orders 9703444625 and 9703476196. Thanks for your help""","Open"],
    ["""m.d.B. to set the final delivery or final invoice indicator => MGTOP / MGTXX - EILT.
    Dear Helpdesk Team,
    May I ask you to complete the following processes with the final delivery indicator and final invoice indicator:
    9705853889
    9705325996
    Thank you very much and have a nice day
    P. Lempe""","Close"],
    ["""Please set final delivery / final invoice - without notifying the supplier - thank you.
    1. 9705888592 Item 1
    2. 9705791121 item 2
    3. 9705648348 Item 2
    ""","Close"],
    ["""FW: Close orders. Could you take care of that, please?


    Important note on centralizing the operational purchasing process:
    Central contact for inquiries about the operational purchasing process:
    * $ PERSON ($ PERSON


    Many Thanks
    With best
    -----
    Close orders


    please close the following orders completely.
    Ask for information if an order cannot be closed.
    Then we make a note of this internally in the master file.

    $ PERSON.

    Lots of $ PERSON $ PERSON 9702506197""","Close"]
    ]
    response= openai.Classification.create(
    search_model="ada",
    model="davinci",
    examples=examples,
    query=mail,
    labels=["Close", "Open"],
    temperature=0.3
    )
    return response["label"]
