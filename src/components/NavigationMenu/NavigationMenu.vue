<template>
  <div class="navigation-menu" :class="{ open: open }">
    <ul class="menu-items-wrapper container">
      <MenuItem
              v-for="(item, index) in menuItems"
              :number="index + 1"
              :key="index"
              :name="item.name"
              :link="item.link"
              :highlight-text="item.highlightText"
              :highlight="highlight === index + 1"
              :construction="item.construction"
              @mouseenter.native="hover(index + 1)"
              @mouseleave.native="hover(0)"
              @close="$emit('close')"
      />
    </ul>
  </div>
</template>

<script>
import MenuItem from "./MenuItem";

export default {
  name: "NavigationMenu",
  components: {
    MenuItem
  },
  props: {
    open: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      highlight: 0,
      menuItems: [
        { name: 'the earth is square', highlightText: 'who are we?', construction: true, link: 'About' },
        { name: 'our portfolio', highlightText: 'history of awesome', construction: true, link: 'Portfolio' },
        { name: 'contact us', highlightText: 'let\'s create', construction: true, link: 'Contact' },
      ]
    }
  },
  methods: {
    hover(num) {
      this.highlight = num
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../styles/variables';

.navigation-menu {
  z-index: 1000;
  position: fixed;
  background-color: #888899;
  width: 100vw;
  height: calc(100vh - 200px);
  transition: left 0.25s ease;
  left: 100%;
  padding-top: 100px;
  padding-bottom: 100px;

  &.open {
    left: 0;
  }

  .menu-items-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
  }
}
</style>