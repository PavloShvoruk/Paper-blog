<template>
  <div id="app">
    <navigation/>
    <router-view/>
  </div>
</template>

<style scoped>
</style>


<script>
import Navigation from "./components/navigation";
import { USER_REQUEST } from "./store/actions/user.js";

export default {
  components: {
    Navigation
  },
  name: "App",
  created() {
    if (this.$store.getters.isAuthenticated) {
      this.$store.dispatch(USER_REQUEST);
    }
  }
};
</script>

<style>
#app {
  margin: 0;
}
</style>
