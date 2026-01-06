package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.domain.user.DataRegister;
import equipo._7.SentimentAPI.domain.user.User;
import equipo._7.SentimentAPI.domain.user.UserRepository;
import equipo._7.SentimentAPI.infra.security.DataTokenJWT;
import equipo._7.SentimentAPI.infra.security.TokenService;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Objects;

@RestController
@RequestMapping("/register")
public class RegisterController {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private AuthenticationManager authenticationManager;
    @Autowired
    private TokenService tokenService;
    @Autowired
    private PasswordEncoder passwordEncoder;

    @Transactional
    @PostMapping
    public DataTokenJWT register(@RequestBody @Valid DataRegister data) {
        System.out.println("Entro");
        if (!Objects.equals(data.password(), data.passwordConfirmation())) {
            throw new RuntimeException("Passwords do not match");
        }
        // TODO: validar que el usuario no exista previamente con mensaje amigable
        var user = new User(data.email(), encodePassword(data.password()));
        userRepository.save(user);
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = authenticationManager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        return new DataTokenJWT(tokenJwt);
    }

    private String encodePassword(String password) {
        return passwordEncoder.encode(password);
    }
}
