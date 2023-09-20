import { StyleSheet, Text, View } from "react-native";

export default function Mic() {
  return <View style={styles.container}></View>;
}

const styles = StyleSheet.create({
  text: {
    fontWeight: "600",
    color: "white",
    fontSize: 24,
  },
  container: {
    backgroundColor: "rgba(40, 0, 168, 0.4)",
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
    paddingVertical: 16,
  },
});
