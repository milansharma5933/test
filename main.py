from fastapi import FastAPI, Form
from pymongo import MongoClient
from pydantic import BaseModel


conn = MongoClient("mongodb+srv://milan:VeQksY01JE6YvXtv@cluster0.q9laqfi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
app = FastAPI()

class Clerk_id(BaseModel):
    userid: str

def get_questions(category):
    return conn.chintachhodo[category].find({})

def fetch_categories(user_id):
    problem = conn.chintachhodo.users.find_one({"clerkId": user_id}, {"_id": 0, "choosedProblems": 1})
    if problem is not None:
        choosed_problems = problem.get("choosedProblems", [])
        print(choosed_problems)
        return choosed_problems
    else:
        print("No document found for the provided clerkId:", user_id)
        return ["Message From Api","Invalid clerkId->",user_id]

#TO CHECK THAT API IS WORKING OR NOT, MAKE GET REQUEST ON THIS ENDPOINT
@app.get("/")
async def read_root():
    return {"Message": "HI! From Milan The api is succesfully deployed and working"}

@app.get("/QnA")
async def selected_categories(user_id:Clerk_id):
    Questions = []
    category=fetch_categories(user_id.userid)
    for j in category:
        query1=get_questions(j)
        for i in query1:
            Questions.append({
                "Q": i["Q"],
                "a": i["A"],
                "b": i["B"],
                "c": i["C"],
                "D": i["D"],
                })
    return Questions

@app.get("/followUpQ")
async def follow_up_ques(Q:str=Form(...)):
    if Q in ["I've been sleeping more than usual", "I've been sleeping less than usual"]:
        return{"Q":"how often does this happen",
               "a":"rarely",
               "b":"sometime",
               "c":"often",
               "d":"all the time"}
