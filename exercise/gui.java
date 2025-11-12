import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ButtonExample extends JFrame implements ActionListener {

    private JButton clickButton;

    public ButtonExample() {
        setTitle("Button Demo");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Center the window

        JPanel panel = new JPanel();
        clickButton = new JButton("Click Me!");
        clickButton.addActionListener(this); // Register this class as the listener

        panel.add(clickButton);
        add(panel);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == clickButton) {
            JOptionPane.showMessageDialog(this, "Button was clicked!");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ButtonExample());
    }
}