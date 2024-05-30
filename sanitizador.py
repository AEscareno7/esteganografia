def remove_message_from_file(file_path):
    # Marcadores de fin de archivo para diferentes formatos
    END_MARKERS = {
        'png': b'\x49\x45\x4E\x44\xAE\x42\x60\x82',  # IEND para PNG
        'jpg': b'\xFF\xD9',  # SOI para JPEG
        'jpeg': b'\xFF\xD9',  # SOI para JPEG
        'pdf': b'\x25\x25\x45\x4F\x46',  # %%EOF para PDF
        'txt': b'',  # No hay marcador específico, usaremos EOF
        'mp3': b'\xFF\xFB'  # No hay un marcador específico estándar, pero FF FB es común
    }

    # Obtener la extensión del archivo
    file_extension = file_path.split('.')[-1].lower()

    if file_extension in END_MARKERS:
        end_marker = END_MARKERS[file_extension]
    else:
        print(f"Formato de archivo '{file_extension}' no soportado.")
        return

    with open(file_path, 'rb') as file:
        content = file.read()

    if file_extension == 'txt':
        # Eliminar cualquier contenido después de la primera línea vacía para TXT
        content_without_message = content.split(b'\n\n')[0] + b'\n\n'
    else:
        # Encontrar el marcador de final de archivo para otros formatos
        end_marker_index = content.rfind(end_marker)
        if end_marker_index != -1:
            # Incluir el tamaño del marcador para mantener la integridad del archivo
            end_marker_index += len(end_marker)
            # Recortar el contenido del archivo hasta el marcador
            content_without_message = content[:end_marker_index]
        else:
            print("No se encontró el marcador de fin de archivo.")
            return

    # Escribir el contenido sin el mensaje en el archivo original
    with open(file_path, 'wb') as file:
        file.write(content_without_message)

    print(f"El mensaje ha sido eliminado del archivo {file_path}")

def display_file_binary(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return content

def main():
    file_path = input("Ingresa la ruta del archivo (PNG, JPEG, PDF, TXT, MP3): ")
    
    # Mostrar el contenido binario antes de eliminar el mensaje
    binary_before = display_file_binary(file_path)
    print("\nContenido binario del archivo antes de eliminar el mensaje:")
    print(binary_before)
    
    remove_message_from_file(file_path)
    
    # Mostrar el contenido binario después de eliminar el mensaje
    binary_after = display_file_binary(file_path)
    print("\nContenido binario del archivo después de eliminar el mensaje:")
    print(binary_after)

if __name__ == "__main__":
    main()
