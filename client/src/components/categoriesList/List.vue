<template>
  <div>
    <div v-for="(category, index) in categories" :key="index">
      <categoryItem :name="category.name"/>
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
  props: ["categories"]
};
</script>

