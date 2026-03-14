import React, { useRef, useEffect } from "react";
import axios from "axios";

function StudentCamera() {
  const videoRef = useRef();

  // Start camera automatically
  useEffect(() => {
    startCamera();
    setInterval(captureAndSend, 2000); // every 2 seconds
  }, []);

  const startCamera = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoRef.current.srcObject = stream;
  };

  const captureAndSend = async () => {
    const canvas = document.createElement("canvas");
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    canvas.getContext("2d").drawImage(videoRef.current, 0, 0);

    const blob = await new Promise(res => canvas.toBlob(res, "image/jpeg"));

    const formData = new FormData();
    formData.append("image", blob);

    await axios.post("http://127.0.0.1:5000/recognize", formData);
  };

  return (
    <div>
      <h2>Classroom Entry Camera</h2>
      <video ref={videoRef} autoPlay width="500" />
    </div>
  );
}

<a href="/admin" style={{position:"absolute", top:10, right:10}}>
  <button>Admin Login</button>
</a>

export default StudentCamera;
