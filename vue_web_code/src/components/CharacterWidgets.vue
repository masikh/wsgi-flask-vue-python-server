<template>
  <div class="container-fluid">
    <h1>Character widgets</h1>

    <dnd-grid-container
      :layout.sync="layout"
      :cell-size="cellSize"
      :max-column-count="maxColumnCount"
      :max-row-count="maxRowCount"
      :margin="margin"
      :bubble-up="bubbleUp"
    >
      <dnd-grid-box
        box-id="settings"
        drag-selector="div.card-header"
        resize-visible="true"
      >
        <div class="card demo-box">
          <div class="card-header">
            Settings
          </div>
          <div class="card-body">
            <div class="form-group row">
              <label
                for="settings-margin-input"
                class="col-sm-4 col-form-label">Margin</label>
              <div class="col-sm-8">
                <input
                  id="settings-margin-input"
                  v-model.number="margin"
                  class="form-control"
                  type="number">
              </div>
            </div>
            <div class="form-group row">
              <label
                for="settings-grid-size-w-input"
                class="col-sm-4 col-form-label">Cell Size</label>
              <div class="col-sm-4">
                <input
                  id="settings-grid-size-w-input"
                  v-model.number="cellSize.w"
                  class="form-control"
                  type="number">
              </div>
              <div class="col-sm-4">
                <input
                  v-model.number="cellSize.h"
                  class="form-control"
                  type="number">
              </div>
            </div>
            <div class="form-group row">
              <label
                for="settings-bubble-up-input"
                class="col-sm-4 col-form-label">Bubble Up</label>
              <div class="col-sm-8">
                <input
                  id="settings-bubble-up-input"
                  v-model="bubbleUp"
                  type="checkbox">
              </div>
            </div>
            <button
              class="btn btn-success"
              @click="boxCount++">Add Box</button>
            <button
              class="btn btn-danger"
              @click="boxCount = Math.max(0, boxCount-1)">Remove Box</button>
          </div>
        </div>
      </dnd-grid-box>
      <dnd-grid-box
        v-for="number in boxCount"
        :box-id="number"
        :key="number"
        drag-selector="div.card-header"
      >
        <div class="card demo-box">
          <div class="card-header">
            Box {{ number }}
          </div>
        </div>
      </dnd-grid-box>
    </dnd-grid-container>
  </div>
</template>

<style>
    .demo-box {
        width: 100%;
        height: 100%;
    }
</style>

<script>
// import Container and Box components
import { Container, Box } from '@dattn/dnd-grid'
// minimal css for the components to work properly
import '@dattn/dnd-grid/dist/dnd-grid.css'

export default {
  components: {
    DndGridContainer: Container,
    DndGridBox: Box
  },

  data () {
    return {
      cellSize: {
        w: 100,
        h: 100
      },
      maxColumnCount: 10,
      maxRowCount: Infinity,
      bubbleUp: false,
      margin: 5,
      boxCount: 1,
      layout: []
    }
  },

  computed: {
    layoutWithoutSettings () {
      return this.layout.filter((box) => {
        return box.id !== 'settings'
      })
    }
  },

  watch: {
    layout: {
      handler: function (oldval, newval) {
        console.log('Layout changed')
        this.saveLayout()
      }
    }

    // layout: newLayout => {
    //  console.log('Layout changed')
    //  handler: function (oldval, newval) {
    //  }
    // }
  },

  created () {
    this.$http.get('/widgets/get').then(response => {
      this.layout = response.data.message
      this.boxCount = this.layout.length
    })
  },

  methods: {
    addWidget () {
      this.boxCount++
    },
    onLayoutUpdate (evt) {
      this.layout = evt.layout
    },
    saveLayout () {
      this.$http.post('/widgets/set', this.layout)
        .then(response => {
          if (response.data.error) {
            this.errorMessage = response.data.error
          }
        })
        .catch(error => {
          this.errorMessage = error.data.message
        })
    }
  }
}
</script>

<style scoped>
.card {
  max-width: 500px;
  padding: 20px;
  background: rgba(255,255,255,1.0);
}

</style>
