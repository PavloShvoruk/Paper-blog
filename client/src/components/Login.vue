<template>
  <div class="row">
    <form class="paper">
      <div class="form-group">
        <h3>Login</h3>
      </div>
      <div class="form-group">
        <input type="text" placeholder="Username">
      </div>
      <div class="form-group">
        <input type="password" placeholder="Password">
      </div>
      <div class="form-group">
        <button class="btn-block">Login</button>
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
export default {
  name: "login"
};
</script>