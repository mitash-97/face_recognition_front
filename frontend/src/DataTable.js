import React, { useEffect, useState } from "react";
import axios from "axios";

function DataTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/data").then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h2>Attendance Data Section</h2>

      <table border="1">
        <thead>
          <tr>
            <th>Photo</th>
            <th>ID</th>
            <th>Entry Times</th>
            <th>Total Entry</th>
            <th>Exit Times</th>
            <th>Total Exit</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {data.map(s => (
            <tr key={s.student_id}>
              <td><img src={`http://127.0.0.1:5000/${s.photo}`} width="60"/></td>
              <td>{s.student_id}</td>
              <td>{s.entry_times}</td>
              <td>{s.total_entries}</td>
              <td>{s.exit_times}</td>
              <td>{s.total_exits}</td>
              <td>{s.status}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <a href="http://127.0.0.1:5000/download">
        <button>Download Excel</button>
      </a>
    </div>
  );
}

export default DataTable;
