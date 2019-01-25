<template>
  <div class="paper">
    <div
      class="child-shadows-hover child-borders"
      v-for="(category, index) in categories"
      :key="index"
    >
      <categoryItem :name="category.name" :description="category.description"/>
    </div>
  </div>
</template>

<style scoped>
.paper {
  margin-right: 5px;
}
</style>

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

