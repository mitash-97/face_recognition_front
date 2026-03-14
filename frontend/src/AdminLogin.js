import React, { useState } from "react";

function AdminLogin() {
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");

  const login = () => {
    if (user === "admin" && pass === "1234") {
      window.location.href = "/dashboard";
    } else {
      alert("Wrong credentials");
    }
  };

  return (
    <div>
      <h2>Admin Login</h2>
      <input placeholder="Username" onChange={e => setUser(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPass(e.target.value)} />
      <button onClick={login}>Login</button>
    </div>
  );
}

export default AdminLogin;
