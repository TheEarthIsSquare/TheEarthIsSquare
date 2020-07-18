<template>
  <li class="menu-item" :class="{ '--construction' : construction }" @click="goPage(link)">
    <div class="menu-item__number">0{{ number }}</div>
    <div class="menu-item__name">
      <transition name="fade">
        <div v-if="!construction" class="menu-item__highlight" v-show="highlight">{{ highlightText }}</div>
        <div v-else class="menu-item__highlight">under construction</div>
      </transition>
      {{ name }}
    </div>
  </li>
</template>

<script>
export default {
  name: "MenuItem",
  props: {
    number: {
      type: Number,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    highlight: {
      type: Boolean,
      default: false
    },
    highlightText: {
      type: String,
      required: true
    },
    construction: {
      type: Boolean,
      default: false
    },
    link: {
      type: String,
      default: 'Home'
    }
  },
  methods: {
    goPage(name) {
      if (!this.construction && this.$route.name !== name) {
        this.$router.push({ name: name })
      }

      this.$emit('close')
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../styles/variables';

.menu-item {
  display: flex;
  align-items: center;
  cursor: pointer;
  margin-bottom: 50px;

  &:last-child {
    margin-bottom: 0;
  }

  &:hover {
    .menu-item__name {
      color: $martinique;
    }
  }

  &.--construction {
    cursor: default;

    &:hover {
      .menu-item__name {
        color: transparent;
      }
    }

    .menu-item__name {
      .menu-item__highlight {
        background-color: $martinique;
      }
    }
  }

  .menu-item__number {
    margin-right: 50px;
    font-size: 24px;
    transform: rotate(-90deg);
    color: $martinique
  }

  .menu-item__name {
    position: relative;
    display: flex;
    align-items: center;
    font-weight: 900;
    font-size: 96px;
    -webkit-text-stroke: 2px #2D2C4E;
    color: transparent;
    transition: color 0.25s ease;

    .menu-item__highlight {
      position: absolute;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      background-color: $rose;
      height: 35%;
      color: white;
      font-size: 42px;
      -webkit-text-stroke: initial;
      margin-top: 20px;

      &.--construction {
        background-color: $martinique;
      }
    }
  }
}
</style>