from fastapi import FastAPI
import uvicorn, os, json

app = FastAPI()


@app.post("/generate")
async def generate(body: dict):
    player_name = body.get("player_name", "")
    char_name = body.get("char_name", "")
    description = body.get("description", "")
    # greeting_message = body.get("greeting_message", "")
    # greeting_message = "<START>\n" + char_name + ":" + greeting_message + " " + player_name + "\n"
    history = body.get("history", "")
    user_input = body.get("user_input", "")

    print(history)
    ai_output = gen(user_input=user_input,
                    player_name=player_name,
                    char_name=char_name,
                    description=description,
                    history=history)

    return {"data": ai_output}


@app.get("/characters")
async def characters():
    character_list = os.listdir("../characters")
    return {"data": character_list}


@app.get("/characters/{character}")
async def get_character(character: str):
    character_file_path = "../characters/" + character
    with open(character_file_path, "r") as f:
        character_info = json.load(f)
    return {"data": character_info}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)