<template>
  <div class="outer-section">
    <section>
      <h1>Cipher or Decipher your text</h1>
      <b-field
        label="Passphrase"
        label-position="on-border">
        <b-input
          v-model="password"
          password-reveal
          required
          placeholder="Your encryption key"
          maxlength="40"
          icon-pack="fas"
          type="password"/>
      </b-field>

      <b-field
        label="Your text"
        label-position="on-border">
        <b-input
          v-model="text"
          placeholder="Your (secret) text"
          maxlength="4000"
          type="textarea"/>
      </b-field>

      <div class="cipher-decipher">
        <div>
          <b-button
            native-type="submit"
            type="is-danger"
            @click="Cipher">
            Cipher
          </b-button>
        </div>
        <div>
          <b-button
            native-type="submit"
            type="is-success"
            @click="Decipher">
            Decipher
          </b-button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

export default {
  data () {
    return {
      text: '',
      password: ''
    }
  },
  computed: {},
  created () {},
  methods: {
    Decipher: function () {
      let params = { 'password': this.password, 'text': this.text }
      this.$http.post('/decipher', params)
        .then(response => {
          if (response.data.error) {
            this.errorMessage = response.data.error
          } else {
            this.text = response.data
          }
        })
        .catch(error => {
          this.errorMessage = error.data.message
        })
    },
    Cipher: function () {
      let params = { 'password': this.password, 'text': this.text }
      this.$http.post('/cipher', params)
        .then(response => {
          if (response.data.error) {
            this.errorMessage = response.data.error
          } else {
            this.text = response.data
          }
        })
        .catch(error => {
          this.errorMessage = error.data.message
        })
    }
  }
}
</script>

<style>
section {
  margin: 25px;
}

.outer-section {
  margin: 125px;
  background: rgba(255,255,255,0.7);
}

.cipher-decipher {
    display: flex;
    justify-content: center;
}

.cipher-decipher > * {
    margin: 5px;
}
</style>
