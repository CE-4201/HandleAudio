import { StyleSheet, Text, View } from "react-native";

export default function Title() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>CE 4202 - IoT Chatbot</Text>
    </View>
  );
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
