from fastapi import FastAPI, HTTPException, status, Path
from fastapi.responses import JSONResponse
from models import Property

app = FastAPI()

properties = {

  1: { 
   'name' : 'Casa no centro',
   'type' : 'Casa',
   'city' : 'Rondonópolis',
   'price': 250000,
   'description': 'Casa com 3 quartos',
   'ownerName' : 'Maria',
   'createdAt' : '03/12/2025' }

}

# Listar todos os imóveis"
@app.get('/properties')
async def get_properties():
    return properties

# Buscar imóvel por ID
@app.get ('/properties/{property_id}')
async def get_property(property_id: int = Path(title="ID do imóvel", gt= 0)):
    if property_id in properties:
      return properties[property_id]
    else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                           detail='Imóvel não encontrado')
    
# Criar novo imóvel
@app.post('/properties', status_code=status.HTTP_201_CREATED)
async def post_property(property:Property):
   next_id: int = len(properties) +1
   
   properties[next_id] = {
      'name' : property.name,
      'type' : property.type,
      'city' : property.city,
      'price': property.price,
      'description' : property.description,
      'ownerName' : property.ownerName,
      'creatdAt' : property.createdAt
   }

   return properties[next_id]
 
#Atualizar imóvel
@app.put('/properties/{property_id}')
async def put_property(property_id: int, property: Property):
   if property_id in properties:
      properties[property_id] ={
         "name": property.name,
         "type": property.type,
         "city": property.city,
         "price": property.price,
         "description": property.description,
         "ownerName": property.ownerName,
         "createdAt": property.createdAt
      }

      return properties[property_id]

   else:
     raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um imóvel com o ID {property_id}'
        )

# Deletar imóvel
@app.delete('/properties/{property_id}')
async def delete_property(property_id: int):
    if property_id in properties:
        del properties[property_id]
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content=None
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um imóvel com o ID {property_id}'
        )