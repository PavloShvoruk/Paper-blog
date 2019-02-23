<template>
  <div>
    <div v-for="(category, index) in categories" :key="index" @click="clickCat(category.name)">
      <categoryItem :categoryName="category.name"/>
    </div>
  </div>
</template>

<script>
import categoryItem from "./Item";

export default {
  components: {
    categoryItem
  },
  name: "categories-list",
  props: {
    categories: Array
  },
  methods: {
    clickCat(name) {
      alert(name);
    }
  }
};
</script>

