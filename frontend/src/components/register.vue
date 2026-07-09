<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-4">
        <div class="card p-4 shadow-sm">
          <h4 class="text-center mb-3">Register</h4>

          <div v-if="alertMessage" :class="['alert', alertClass]" role="alert">
            {{ alertMessage }}
          </div>

          <form @submit.prevent="register">
            <div class="mb-3">
              <label class="form-label">Username</label>
              <input v-model="username" type="text" class="form-control" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input v-model="email" type="email" class="form-control" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Password</label>
              <input v-model="password" type="password" class="form-control" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Role</label>
              <select v-model="role" class="form-select" required>
                <option value="student">Student</option>
                <option value="company">Company</option>
              </select>
            </div>
            <button type="submit" class="btn btn-success w-100">Register</button>
          </form>

          <p class="text-center mt-3">
            Already have an account?
            <router-link to="/login" class="text-decoration-none">Login</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//console.log(decoded);

export default {
  name: "RegisterPage",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      role: "student",
      alertMessage: "",
      alertClass: ""
    };
  },
  methods: {
    async register() {
      try {
        const role_id = this.role === "student" ? 2 : 3; // backend expects numeric role_id

        const res = await fetch("http://localhost:5000/api/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password,
            role_id: role_id
          })
        });

        const data = await res.json();
        if (!res.ok) {
          this.alertMessage = data.msg || "Registration failed.";
          this.alertClass = "alert-danger";
          return;
        }

        this.alertMessage = "Registration successful!";
        this.alertClass = "alert-success";
      } catch (err) {
        this.alertMessage = "Network error.";
        this.alertClass = "alert-danger";
      }
    }
  }
};
</script>
