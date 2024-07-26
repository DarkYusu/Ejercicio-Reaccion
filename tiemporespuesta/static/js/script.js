const letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];
    let letraActual;
    let tiempos = [];
    let tiemposInicio = [];
    let pruebaIndex = 0;

    // Mostrar una nueva letra
    function mostrarLetra() {
        letraActual = letras[Math.floor(Math.random() * letras.length)];
        document.getElementById('letra').innerText = letraActual;
        tiemposInicio[pruebaIndex] = new Date().getTime(); // Guardar el tiempo de inicio
    }

    // Guardar los resultados al ingresar una letra
    function guardarResultado() {
        const inputLetra = document.getElementById('input-letra').value.toUpperCase();
        const tiempoFin = new Date().getTime();
        const tiempo = (tiempoFin - tiemposInicio[pruebaIndex]) / 1000; // Tiempo en segundos

        if (inputLetra === letraActual) {
            tiempos.push(tiempo);
        } else {
            tiempos.push(0);
        }

        pruebaIndex++;
        document.getElementById('input-letra').value = '';

        if (pruebaIndex < 5) {
            mostrarLetra();
        } else {
            // Mostrar botón para ver resultados
            document.getElementById('ver-resultados-btn').style.display = 'block';
            document.getElementById('mensaje').innerText = 'Prueba completada. Puedes ver tus resultados.';
        }
    }

    // Manejar el evento de entrada de texto
    document.getElementById('input-letra').addEventListener('input', guardarResultado);

    // Manejar el evento del botón para ver resultados
    document.getElementById('ver-resultados-btn').addEventListener('click', () => {
        fetch('/guardar-prueba/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                letra_1: letras[0],
                tiempo_1: tiempos[0],
                letra_2: letras[1],
                tiempo_2: tiempos[1],
                letra_3: letras[2],
                tiempo_3: tiempos[2],
                letra_4: letras[3],
                tiempo_4: tiempos[3],
                letra_5: letras[4],
                tiempo_5: tiempos[4]
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = '/mi-puntuacion/'; // Redirigir a la página de puntuación
            } else {
                document.getElementById('mensaje').innerText = 'Error al guardar la prueba.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('mensaje').innerText = 'Error al guardar la prueba.';
        });
    });

    // Inicializar la prueba
    mostrarLetra();
    
document.getElementById('submit-btn').addEventListener('click', () => {
    const inputLetra = document.getElementById('input-letra').value.toUpperCase();
    const tiempoFin = new Date().getTime();
    const tiempo = (tiempoFin - tiemposInicio[pruebaIndex]) / 1000;

    if (inputLetra === letraActual) {
        tiempos.push(tiempo);
    } else {
        tiempos.push(0);
    }

    pruebaIndex++;
    document.getElementById('input-letra').value = '';

    if (pruebaIndex < 5) {
        mostrarLetra();
    } else {
        fetch('/ruta-para-guardar-prueba/', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                letra_1: letras[0],
                tiempo_1: tiempos[0],
                letra_2: letras[1],
                tiempo_2: tiempos[1],
                letra_3: letras[2],
                tiempo_3: tiempos[2],
                letra_4: letras[3],
                tiempo_4: tiempos[3],
                letra_5: letras[4],
                tiempo_5: tiempos[4]
            })
        }).then(response => response.json())
        .then(data => {
            document.getElementById('mensaje').innerText = 'Prueba completada y guardada.';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
mostrarLetra();
