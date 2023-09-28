# pylectormanga
pylectormanga es una biblioteca que te permite buscar manga disponible a través de [lectormanga](https://lectormanga.com/). Y podrás acceder a su información.

## Instalación
```sh
pip install pylectormanga
```
## Uso
La biblioteca contiene la función `search` para buscar manga disponible y el objeto `PyLectorManga`, que tiene el parámetro url que se pasará para acceder a la información completa del manga.

A continuación te muestro cómo funciona:

```python
from pylectormanga import search
from pylectormanga import PyLectorManga

title   = str(input("Introduce el nombre del manga: "))
results = search(title)

if results == []:
    print("No encontramos resultados.")
else:
    print("\nEncontramos resultados: ")
    for i, result in enumerate(results):
        print(f"{i+1}. {result['title']} - {result['type']}")
    
    index = int(input("\nIngresa un numero del manga al que deseas acceder: "))
    information_manga = PyLectorManga(results[index - 1]['url'])

    print('\n1. Información sobre el manga.')
    print('2. Obtener todos los capítulos del manga.')
    print('3. Obtener un capítulo específico.')

    value = int(input("\nIntroduce un valor en el que quieras al acceder al menú: "))

    match(value):
        case 1:
            manga = information_manga.get_manga_information()

            print(f"\nTítulo: {manga['title']}")
            print(f"Descripción: {manga['description']}")
            print(f"Géneros: {manga['genre']}\n")
        case 2:
            for chapter in information_manga.get_all_the_chapters():
                print(f"\nTítulo: {chapter['title']}")
                print(f"Fecha: {chapter['date']}")
                print(f"Ver manga: {chapter['url']}")
        case 3:
            chapter = str(input("Por favor ingresa el capítulo donde deseas obtener tu información. (Ejemplo 120.00): "))
            manga = information_manga.get_one_chapter(chapter)

            if not manga:
                print("\nNo encontramos resultados.")
            else:
                print(f"\nTítulo: {manga['title']}")
                print(f"Fecha: {manga['date']}")
                print(f"Ver manga: {manga['url']}")
```
## Motivo
Todo surgió cuando estaba viendo mi anime favorito Tokyo Revengers.