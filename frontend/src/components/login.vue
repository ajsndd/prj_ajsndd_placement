<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-4">
        <div class="card p-4 shadow-sm">
          <h4 class="text-center mb-3">Login</h4>

          <div v-if="alertMessage" :class="['alert', alertClass]" role="alert">
            {{ alertMessage }}
          </div>

          <form @submit.prevent="login">
            <div class="mb-3">
              <label class="form-label">Username</label>
              <input v-model="username" type="text" class="form-control" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Password</label>
              <input v-model="password" type="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Login</button>
          </form>

          <p class="text-center mt-3">
            Don't have an account?
            <router-link to="/register" class="text-decoration-none">Register</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import jwtDecode from "jwt-decode"; // install with npm install jwt-decode


export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: "",
      alertMessage: "",
      alertClass: ""
    };
  },
  methods: {
    async login() {
      try {
        const res = await fetch("http://localhost:5000/api/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });

        const data = await res.json();
        if (!res.ok) {
          this.alertMessage = data.msg || "Login failed.";
          this.alertClass = "alert-danger";
          return;
        }

        // Save token
        localStorage.setItem("token", data.access_token);

        // Decode JWT to get role
        const decoded = jwtDecode(data.access_token);
        const role = decoded.role; // backend must include role in JWT claims
        console.log(decoded);
        // Redirect based on role
        if (role === "admin") this.$router.push("/admin");
        else if (role === "company") this.$router.push("/company");
        else this.$router.push("/student");

      } catch (err) {
        this.alertMessage = "Network error.";
        this.alertClass = "alert-danger";
      }
    }
  }
};
</script>
