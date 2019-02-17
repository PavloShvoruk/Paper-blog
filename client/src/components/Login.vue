<template>
  <div class="row">
    <form @submit.prevent="formSubmitted = true" class="paper">
      <div class="form-group">
        <h3>Login</h3>
      </div>
      <div class="form-group" v-if="alert">
        <div class="alert alert-danger">{{ error }}</div>
      </div>
      <div class="form-group">
        <input v-model="username" type="text" placeholder="Username">
      </div>
      <div class="form-group">
        <input v-model="password" type="password" placeholder="Password">
      </div>
      <div class="form-group">
        <button class="btn-block" @click="login">Login</button>
        <!-- <button class="btn-block" @click="onClick">Facebook</button> -->
      </div>
      <div class="form-group">
        <p class="text-muted">Not registered?
          <router-link to="/register">Create an account</router-link>
        </p>
      </div>
    </form>
  </div>
</template>

<style scoped>
.row {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - 70px);
}

.form-group > h3 {
  text-align: center;
}

.form-group > input {
  width: 100%;
}
</style>

<script>
import { AUTH_REQUEST } from "../store/actions/auth.js";
import ApiService from "../ApiService.js";
import Axios from "axios";

export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      error: "",
      alert: false
    };
  },
  methods: {
    async onClick() {
      try {
        await ApiService.getUser().then(resp => {
          console.log(resp);
        });
      } catch (error) {
        console.log(error.message);
      }
    },
    login() {
      const { username, password } = this;
      this.$store
        .dispatch(AUTH_REQUEST, { username, password })
        .then(() => {
          this.$router.push("/");
        })
        .catch(() => {
          if (this.$store.state.auth.status === 400) {
            this.error = "Wrong credentials";
            this.alert = true;
            this.username = "";
            this.password = "";

            setTimeout(() => {
              this.alert = false;
            }, 5000);
          }
        });
    }
  }
};
</script>