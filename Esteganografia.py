def add_message_to_file(file_path, message):
    with open(file_path, 'ab') as file:
        file.write(b'\n')  # Añade una nueva línea para separar el mensaje del contenido original
        file.write(message.encode('utf-8'))
        file.write(b'\n')  # Añade una nueva línea para marcar el final del mensaje

def read_message_from_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        
    # Busca el último mensaje separado por nuevas líneas
    if b'\n' in content:
        parts = content.split(b'\n')
        message = parts[-2].decode('utf-8')  # El penúltimo elemento es el mensaje
        return message
    return None

def display_file_binary(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        return content

def main():
    file_path = input("Ingresa la ruta del archivo (imagen o video): ")
    
    # Mostrar el contenido binario antes de agregar el mensaje
    binary_before = display_file_binary(file_path)
    print("\nContenido binario del archivo antes de agregar el mensaje:")
    print(binary_before)
    
    message = input("Ingresa el mensaje que deseas añadir al archivo: ")
    add_message_to_file(file_path, message)
    
    # Mostrar el contenido binario después de agregar el mensaje
    binary_after = display_file_binary(file_path)
    print("\nContenido binario del archivo después de agregar el mensaje:")
    print(binary_after)
    
    # Leer y mostrar el mensaje añadido
    read_message = read_message_from_file(file_path)
    if read_message:
        print(f"\nMensaje encontrado en el archivo: {read_message}")
    else:
        print("\nNo se encontró ningún mensaje en el archivo.")

if __name__ == "__main__":
    main()
