const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3000;

// Ruta para servir la página HTML
app.get('/', (req, res) => {
  // Envía el archivo HTML al cliente
  res.sendFile(__dirname + '/index.html');
});

// Ruta para abrir VLC con la URL RTSP
app.get('/openVLC', (req, res) => {
  const urlRTSP = 'rtsp://tapovichin:tapovichin@192.168.1.75:554/stream1';
  const vlcPath = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"';
  const command = `${vlcPath} ${urlRTSP}`;

  // Ejecuta el comando para abrir VLC
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error ejecutando VLC: ${error.message}`);
      res.status(500).send('Error al abrir VLC');
      return;
    }
    if (stderr) {
      console.error(`Error ejecutando VLC: ${stderr}`);
      res.status(500).send('Error al abrir VLC');
      return;
    }
    console.log(`VLC se ha abierto correctamente`);
    res.send('VLC se ha abierto correctamente');
  });
});

// Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});

