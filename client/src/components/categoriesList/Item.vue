<template>
  <div class="title">
    <h4>{{ name }}</h4>
  </div>
</template>
<style scoped>
.title {
  cursor: pointer;
}
</style>

<script>
export default {
  name: "category-item",
  props: ["name"]
};
</script>