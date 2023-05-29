from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Persona (BaseModel):
    id: int
    nombre: str
    edad: int
    ciudad: Optional[str] = None

personaList = []

@app.post("/personas", response_model=Persona)
def crear_persona(person: Persona):
    personaList.append(person)
    return person

@app.get("/personas", response_model=List[Persona])
def get_personas():
    return personaList

@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona (persona_id: int):
    for persona in personaList:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.delete("/personas/{persona_id}")
def eliminar_persona (persona_id: int):
    persona = next((p for p in personaList if p.id == persona_id), None)
    if persona:
        personaList.remove(persona)
        return {"mensaje": "Persona eliminada exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.get("/")
def read_root():
    return {"Hello": "Interoperabilidad 8"}
