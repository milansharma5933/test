from fastapi import FastAPI, Form
from pymongo import MongoClient
from pydantic import BaseModel


conn = MongoClient("mongodb+srv://milansharma5933:testdbpassword@cluster0.0h4jzcw.mongodb.net/")
app = FastAPI()

class Item(BaseModel):
    userid: str

def get_questions(category):
    return conn.Question[category].find({})

@app.get("/")
async def read_root():
    return {"HI": "HI"}

@app.post("/")
async def create_item(item:Item):
    print(item)
    return item

@app.get("/QnA")
async def selected_categories(Anxiety: bool = Form(False),
                                Stress: bool = Form(False),
                                  Depression: bool = Form(False),
                                    Anger: bool = Form(False),
                                      Sleeping: bool = Form(False)):
    Questions = []
    if Anxiety:
        query1 = get_questions("Anxiety")
        for i in query1:
            Questions.append({
                "Q": i["Q"],
                # "a": i["A"],
                # "b": i["B"],
                # "c": i["C"],
                # "D": i["D"],
            })
    if Stress:
        query2 = get_questions("Stress")
        for i in query2:
            Questions.append({
                "Q": i["Q"],
                # "a": i["A"],
                # "b": i["B"],
                # "c": i["C"],
                # "d": i["D"],
            })
    if Depression:
        query3 = get_questions("Depression")
        for i in query3:
            Questions.append({
                "Q": i["Q"],
                # "a": i["A"],
                # "b": i["B"],
                # "c": i["C"],
                # "d": i["D"],
            })
    if Anger:
        query4 = get_questions("Anger")
        for i in query4:
            Questions.append({
                "Q": i["Q"],
                # "a": i["A"],
                # "b": i["B"],
                # "c": i["C"],
                # "d": i["D"],
            })
    if Sleeping:
        query5 = get_questions("Sleeping")
        for i in query5:
            Questions.append({
                "Q": i["Q"],
                # "a": i["A"],
                # "b": i["B"],
                # "c": i["C"],
                # "d": i["D"],
            })
    return {"message": Questions}

@app.get("/followUpQ")
async def follow_up_ques(Q:str=Form(...)):
    if Q in ["I've been sleeping more than usual", "I've been sleeping less than usual"]:
        return{"Q":"how often does this happen",
               "a":"rarely",
               "b":"sometime",
               "c":"often",
               "d":"all the time"}
