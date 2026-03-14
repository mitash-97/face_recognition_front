import React, { useRef, useState } from "react";
import axios from "axios";

function Registration() {
  const videoRef = useRef();
  const [id, setId] = useState("");

  const startCamera = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoRef.current.srcObject = stream;
  };

  const capture = async () => {
    const canvas = document.createElement("canvas");
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    canvas.getContext("2d").drawImage(videoRef.current, 0, 0);
    const blob = await new Promise(res => canvas.toBlob(res, "image/jpeg"));

    const formData = new FormData();
    formData.append("image", blob);
    formData.append("id", id);

    await axios.post("http://127.0.0.1:5000/register", formData);
    alert("Registered");
  };

  return (
    <div>
      <h2>Registration Section</h2>
      <video ref={videoRef} autoPlay width="300" />
      <br />
      <button onClick={startCamera}>Start Camera</button>
      <input placeholder="Student ID" onChange={e => setId(e.target.value)} />
      <button onClick={capture}>Register Student</button>
    </div>
  );
}

export default Registration;
