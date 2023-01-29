<template>
  <HomePanel :rowSpan="isDesktop ? '5' : '6'" colSpan="12" isExternalLink midGap="1rem" to="https://upleveled.io">
    <template v-slot:bg>
      <Duotone color="Green">
        <img alt="Students learning to code." src="~/assets/img/upleveled_8_2bit.avif"/>
      </Duotone>
    </template>

    <Heading type="h4">Powered By</Heading>
    <img alt="UpLeveled Logo" src="~/assets/img/upleveled_logo.png"/>
    <CoreButton variant="secondary">
      Stalk Them
    </CoreButton>
  </HomePanel>
</template>

<script lang="ts" setup>
import { useScreen } from "~/hooks/useScreen";

const { isDesktop } = useScreen();
</script>