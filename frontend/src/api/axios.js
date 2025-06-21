import axios from "axios";

const token = localStorage.getItem('token');

const instance = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
    ...(token && { Authorization: `Bearer ${token}` })
  },
});

export default instance;
