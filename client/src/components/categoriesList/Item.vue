<template>
  <div class="category-item">
    <h4 class="title">{{ name }}</h4>
    <h5 class="text-secondary">{{ description }}</h5>
  </div>
</template>

<style scoped>
.category-item {
  text-align: center;
  line-height: 8px;
  margin-bottom: 10px;
  width: 20rem;
  cursor: pointer;
}
</style>

<script>
export default {
  name: "category-item",
  props: ["name", "description"]
};
</script>