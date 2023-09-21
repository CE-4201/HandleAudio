import { StyleSheet, Text, View, Image } from "react-native";

export default function Loading({ align }: { align: "left" | "right" }) {
  return (
    <View
      style={align === "left" ? styles.leftContainer : styles.rightContainer}
    >
      <Image source={require("../assets/loading.gif")} style={styles.gif} />
    </View>
  );
}

const styles = StyleSheet.create({
  gif: {
    height: 50,
    width: 50,
  },
  leftContainer: {
    paddingHorizontal: 16,
    alignItems: "flex-start",
    justifyContent: "center",
    width: "100%",
  },
  rightContainer: {
    paddingHorizontal: 16,
    alignItems: "flex-start",
    justifyContent: "center",
    width: "100%",
  },
});
