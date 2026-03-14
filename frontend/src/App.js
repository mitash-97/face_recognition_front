import { BrowserRouter, Routes, Route } from "react-router-dom";
import StudentCamera from "./StudentCamera";
import AdminLogin from "./AdminLogin";
import AdminDashboard from "./AdminDashboard";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<StudentCamera />} />
        <Route path="/admin" element={<AdminLogin />} />
        <Route path="/dashboard" element={<AdminDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
