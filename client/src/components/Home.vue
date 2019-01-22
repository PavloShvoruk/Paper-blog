<template>
  <div>
    <ul v-for="(category, index) in categoryList" :key="index">
      <li>{{ category.name }}</li>
    </ul>
  </div>
</template>

<script>
// import ApiService from "../ApiService.js";
import { store } from "vuex";

export default {
  name: "home",
  mounted() {
    try {
      this.$store.dispatch("GET_CATEGORIES");
    } catch (error) {
      console.log(error.message);
    }
  },
  computed: {
    categoryList() {
      return this.$store.getters.CATEGORIES;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
