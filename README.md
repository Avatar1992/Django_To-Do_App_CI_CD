Django To-Do App (CI/CD with Jenkins, Dockerin and Doker out)

Checkout → pulls your repo.

Deps (docker‑in) → runs a short step inside a Python container to ensure deps resolve (no tests).

Build (docker‑out) → builds the app image on the host with Docker.

Run (docker‑out) → replaces any old container and runs the new image on port 8000.

 <img width="1498" height="799" alt="Screenshot from 2025-08-21 20-28-48" src="https://github.com/user-attachments/assets/b516efbe-26d3-409f-a12f-b38beec6a0ac" />





