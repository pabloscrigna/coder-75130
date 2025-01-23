console.log("Iniciando el consumidor...");

// Realizar una solicitud GET a la ruta /health-check del servidor

fetch("http://127.0.0.1:8000/health")
  .then((response) => {
    // Imprimir el código de estado de la respuesta
    console.log("Código de estado:", response.status);
    if (!response.ok) {
      throw new Error(`Error en la solicitud: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    console.log("Respuesta del servidor:", data);
    // Aquí puedes manejar la respuesta, por ejemplo, actualizar la interfaz de usuario
  })
  .catch((error) => {
    console.error("Hubo un problema con la solicitud fetch:", error);
  });

console.log("Consumidor finalizado.");
