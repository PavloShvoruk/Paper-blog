<template>
  <ul>
    <li
      v-for="(category, index) in categories"
      :key="index"
    >{{category.name }}, {{ category.description }}</li>
  </ul>
</template>

<script>
import ApiService from "../ApiService.js";

export default {
  name: "home",
  data() {
    return {
      categories: []
    };
  },
  async created() {
    try {
      this.categories = await ApiService.getCategories();
    } catch (error) {
      console.log(error.message);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
