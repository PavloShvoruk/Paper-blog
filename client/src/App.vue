<template>
  <div id="app">
    <navigation/>
    <!-- <div class="wrapper"> -->
    <router-view/>
    <!-- </div> -->
  </div>
</template>

<script>
import Navigation from "./components/navigation";

export default {
  components: {
    Navigation
  },
  name: "App"
};
</script>

<style>
#app {
  margin: 0;
}
</style>
