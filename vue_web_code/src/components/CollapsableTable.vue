<template>
  <section>
    <b-collapse
      :open="open"
      animation="slide"
      aria-id="contentId"
      class="panel">
      <div
        slot="trigger"
        aria-controls="contentId"
        class="panel-heading"
        role="button">
        <strong>{{ title }}</strong>
      </div>
      <div class="panel-block">
        <b-table
          :columns="columns"
          :data="data"
          class="table"
          striped
          @select="select"/>
      </div>
    </b-collapse>
  </section>
</template>

<script>
export default {
  name: 'CollapsableTable',
  props: {
    title: {
      type: String,
      default: ''
    },
    columns: {
      type: Array,
      default: () => []
    },
    data: {
      type: Array,
      default: () => []
    },
    open: {
      type: Boolean,
      default: false
    },
    select: {
      type: Function,
      default: () => {
      }
    }
  }
}
</script>

<style scoped>
.panel-block {
  text-align: left;
}
.table {
  width: 100%;
}
</style>
